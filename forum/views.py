from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Answer, Question


class QuestionListView(ListView):
    model = Question
    template_name = "forum/question_list.html"
    context_object_name = "questions"
    paginate_by = 10

    def get_queryset(self):
        queryset = Question.objects.all()
        sort_option = self.request.GET.get("sort", "latest")  # Default to 'latest'

        if sort_option == "my-posts":
            queryset = queryset.filter(author=self.request.user)
        else:
            queryset = queryset.order_by("-created_at")  # Sort by latest first

        return queryset


class QuestionDetailView(DetailView):
    model = Question
    template_name = "forum/question_detail.html"
    context_object_name = "question"


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = "forum/question_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("forum:question_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    template_name = "forum/answer_create.html"
    fields = ["content"]

    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.kwargs["pk"])
        form.instance.question = question
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        question = get_object_or_404(Question, pk=self.kwargs["pk"])
        return reverse_lazy("forum:question_detail", kwargs={"pk": question.pk})


# View for handling delete requests
def delete_question(request, pk):
    # Retrieve the question or return 404 if not found
    question = get_object_or_404(Question, pk=pk)

    # Check if the logged-in user is the author of the question
    if question.author != request.user:
        return HttpResponseForbidden(
            "You do not have permission to delete this question."
        )

    # Only allow DELETE requests
    if request.method == "DELETE":
        question.delete()  # Delete the question
        return JsonResponse({"success": True})  # Return success response

    # Return a failure response if method is not DELETE
    return JsonResponse({"success": False, "message": "Invalid method"})


def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)

    # Handle like or unlike action
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
        liked = False
    else:
        answer.likes.add(request.user)
        liked = True

    # Return the updated like count and the liked status
    return JsonResponse({"liked": liked, "count": answer.likes.count()})

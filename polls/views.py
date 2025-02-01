from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, ChoiceQuestion


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["selected_choices"] = set(ChoiceQuestion.objects.filter(
            question_id=self.object.pk
        ).values_list("choice_id", flat=True))
        context["choices"] = Choice.objects.all()

        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.object  # Acceder a la instancia de la pregunta correctamente

        # Obtener opciones con votos
        choices_with_text = ChoiceQuestion.objects.filter(question=question).annotate(
            choice_text=F("choice__choice_text")
        ).values("choice_text", "votes")

        if not choices_with_text.exists():
            context["error_message"] = "No hay votos para esta pregunta."

        context["choices_with_text"] = choices_with_text
        return context


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = get_object_or_404(Choice, pk=request.POST["choice"])
        choice_question = ChoiceQuestion.objects.create(
            question=question, choice=selected_choice)
    except (KeyError, ChoiceQuestion.DoesNotExist):
        # Si el usuario no seleccionó una opción válida, mostramos un error
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a valid choice.",
            },
        )
    else:
        # 1️⃣ Incrementar el número de votos en ChoiceQuestion
        choice_question.votes = F("votes") + 1
        choice_question.save()

        # 2️⃣ Redirigir a la página de resultados
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

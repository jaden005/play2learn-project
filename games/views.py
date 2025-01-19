import json
from django.http import JsonResponse

from django.views.generic import CreateView, DeleteView, TemplateView
from games.models import GameScore
from games.forms import GameScoreForm


class AnagramHuntView(TemplateView):
    model = GameScore
    template_name = 'games/anagram-hunt.html'

    def get_context_data(self, **kwargs):
        context = super(AnagramHuntView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')[0:3]
        return context
    

class AnagramScoresView(TemplateView):
    template_name="games/anagram_scores.html"

    def get_context_data(self, **kwargs):
        context = super(AnagramScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context
    

class MyAHScoresView(TemplateView):
    template_name = 'games/my_ah_scores.html'

    def get_context_data(self, **kwargs):
        context = super(MyAHScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM', user=self.request.user).order_by('-end_time')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH', user=self.request.user).order_by('-end_time')
        return context


class MathFactsView(TemplateView):
    model = GameScore
    template_name = "games/math-facts.html"

    def get_context_data(self, **kwargs):
        context = super(MathFactsView, self).get_context_data(**kwargs)
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')[0:3]   
        return context


class MathScoresView(TemplateView):
    template_name="games/math_scores.html"

    def get_context_data(self, **kwargs):
        context = super(MathScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context
    

class MyMFScoresView(TemplateView):
    template_name = 'games/my_mf_scores.html'

    def get_context_data(self, **kwargs):
        context = super(MyMFScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM', user=self.request.user).order_by('-end_time')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH', user=self.request.user).order_by('-end_time')
        return context


class MyScoresView(TemplateView):
    template_name = 'games/my_scores.html'

    def get_context_data(self, **kwargs):
        context = super(MyScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM', user=self.request.user).order_by('-score')[0:3]
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH', user=self.request.user).order_by('-score')[0:3]
        return context


class GameScoresView(TemplateView):
    template_name="games/game_scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')[0:3]
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')[0:3]
        return context


def record_score(request):
    data = json.loads(request.body)

    game = data["game"]
    score = data["score"]
    max_number = data["max_number"]
    operation = data["operation"]
    user_id = request.user.id
    
    new_score = GameScore(game=game, score=score, max_number=max_number, operation=operation, user_id=user_id)
    new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)




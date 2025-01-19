from django.urls import path

from games.views import (MathFactsView, AnagramHuntView, 
    GameScoresView, record_score,
    MathScoresView, AnagramScoresView,                 
    MyScoresView, MyMFScoresView, MyAHScoresView
)

from pages.views import HomePageView

app_name = 'games'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('record-score/', record_score, name="record-score"),
    path('game_scores/', GameScoresView.as_view(), name="game-scores"),
    path('math-scores/', MathScoresView.as_view(), name="math-scores"),
    path('anagram-scores/', AnagramScoresView.as_view(), name="anagram-scores"),
    path('my-scores/', MyScoresView.as_view(), name='my-scores'),
    path('my-mf-scores/', MyMFScoresView.as_view(), name='my-mf-scores'),
    path('my-ah-scores/', MyAHScoresView.as_view(), name='my-ah-scores'),
]
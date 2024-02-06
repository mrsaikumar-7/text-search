# paragraph/urls.py
from django.urls import path
from .views import ParagraphListCreateView, ParagraphRetrieveUpdateDestroyView, search_paragraphs

# Define URL patterns for the Paragraph app
urlpatterns = [
    # URL pattern for listing and creating paragraphs
    path('paragraphs/', ParagraphListCreateView.as_view(), name='paragraph-list-create'),

    # URL pattern for retrieving, updating, and deleting a specific paragraph
    path('paragraphs/<int:pk>/', ParagraphRetrieveUpdateDestroyView.as_view(), name='paragraph-retrieve-update-destroy'),

    # URL pattern for searching paragraphs containing a specific word
    path('search/<str:word>', search_paragraphs, name='search-paragraphs'),
    # Add more URLs as needed
]

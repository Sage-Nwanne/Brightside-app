from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

MOODS = {
    'M': {
        'label': 'Motivated',
        'emoji': '💪',
        'color': '#06D6A0',
    },
    'H': {
        'label': 'Happy',
        'emoji': '😊',
        'color': '#FFD93D',
    },
    'S': {
        'label': 'Sad',
        'emoji': '😢',
        'color': '#4A90E2',
    },
    'A': {
        'label': 'Angry',
        'emoji': '😠',
        'color': '#FF6B6B',
    },
    'N': {
        'label': 'Neutral',
        'emoji': '😐',
        'color': '#A0A0A0',
    },
    'G': {
        'label': 'Grateful',
        'emoji': '🙏',
        'color': '#FFCA3A',
    },
    'C': {
        'label': 'Content',
        'emoji': '🧘',
        'color': '#70D6FF',
    },
    'E': {
        'label': 'Excited',
        'emoji': '🤩',
        'color': '#FF9F1C',
    },
    'T': {
        'label': 'Tired',
        'emoji': '😴',
        'color': '#BDB2FF',
    },
    'O': {
        'label': 'Overwhelmed',
        'emoji': '😵',
        'color': '#7209B7',
    },
    'R': {
        'label': 'Reflective',
        'emoji': '🤔',
        'color': '#80ED99',
    },
    'B': {
        'label': 'Bored',
        'emoji': '😐',
        'color': '#D3D3D3',
    }
}


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    mood = models.CharField(
        max_length=1,
        choices=[(key, MOODS[key]['label']) for key in MOODS.keys()],
        default='C'
    )
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'entry_id': self.id})

class Comments(models.Model):
    content = models.TextField('Comment')
    created_at = models.DateTimeField(auto_now_add=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} commented: {self.content }"
    
    class Meta:
        ordering = ['-created_at']
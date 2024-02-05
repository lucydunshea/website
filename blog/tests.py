from django.test import TestCase
from blog.models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title='blog 1',
                            body='content for blog 1.',
                            )
        Post.objects.create(title='blog 2',
                            body='content for blog 2.')
        
    def test_post_bodies_align(self):
        """post bodies match the title of the post"""
        first = Post.objects.get(title='blog 1')
        second = Post.objects.get(title='blog 2')
        self.assert_(first != second)

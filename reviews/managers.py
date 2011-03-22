from django.contrib.auth.models import User
from django.db import models


class VoteManager(models.Manager):
    
    def likes(self):
        """
        Returns a QuerySet of the votes for a Review.
        """
        return self.get_query_set().filter(like=True)
    
    def dislikes(self):
        """
        Returns a QuerySet of the votes against a Review.
        """
        return self.get_query_set().filter(like=False)
    
    def likes_count(self):
        """
        Returns the number of the votes for a Review.
        """
        return self.get_query_set().filter(like=True).count()
    
    def dislikes_count(self):
        """
        Returns the number of the votes against a Review.
        """
        return self.get_query_set().filter(like=False).count()


class ReviewedItemManager(models.Manager):
    """
    Allows Reviews to be listed and sorted by various criteria.
    """
    
    def average_rating(self):
        """
        Return the average rating out of 5 for the ReviewedItem.
        """
        reviews = self.get_query_set()
        num_reviews = reviews.all().count()
        total_stars = 0
        if num_reviews == 0:
            return 0
        for r in reviews.all():
            total_stars += r.score
        return float(total_stars) / num_reviews
    
    def average_rating_percentage(self):
        """
        Return the average rating percentage for the ReviewedItem.
        """
        reviews = self.get_query_set()
        num_reviews = reviews.all().count()
        total_stars = 0
        if num_reviews == 0:
            return 0
        for r in reviews.all():
            total_stars += r.score
        possible_stars = num_reviews * 5
        return (total_stars * 100) / float(possible_stars)
    
    
    # TODO: Add get_rating
    
    # def get_for_user(self, user):
    #     try:
    #         return self.get_query_set().filter(user__pk=user.id)
    #     except:
    #         return None

    # def get_for_instance(self, user):
    #     try:
    #         return self.get_query_set().filter(user__pk=user.id)
    #     except:
    #         return None
"""
get_reviews_for_user
get_reviews_for_model
get_reviews_for_model_instance
"""
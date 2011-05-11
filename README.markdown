# django-reviews

## Description

A pluggable Django review app.

Easily integrate reviews in your Django models, including these features:

- **Review and Rating**: Authenticated users can post Reviews of a model including a review text area and a score ()
- **Vote on a Review**: Allows users to vote for or against a Review if it was helpful to them (e.g. "Was this review helpful to you? Yes or No"). Votes store the user's IP address, user (if they are authenticated), whether they liked the review or not


## Usage

0. Install django-reviews:

        pip install -e git://github.com/danawoodman/django-reviews.git#egg=django-reviews

0. Put `reviews` in your `INSTALLED_APPS` tuple in `settings.py`:

        INSTALLED_APPS = (
            #...
            'reviews',
            #...
        )

0. Run `syncdb`:

        ./manage.py syncdb

0. Put reviews in your models:

    from reviews.models import ReviewedItem
    
    class Product(models.Model):
        #...other fields here...
        reviews = generic.GenericRelation(ReviewedItem)

Now you can use all the features of the Review app on your model.


### Manager methods




## Credits

Copyright &copy; 2011 [Dana Woodman](http://www.danawoodman.com/) ([email me](dana@danawoodman.com)).


## Dependencies

None.


## To-do

- Generic views for adding a Review/Vote.
- Write tests (someday...)

Please feel free to fork the repo and add these features if you feel up to it.


## License

Released under an MIT license. See the `LICENSE` file for more information.

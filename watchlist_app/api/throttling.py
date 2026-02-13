from rest_framework.throttling import UserRateThrottle


# Here we just need to define our scope.
class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'
    
class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'exercises',   views.ExerciseViewSet)
router.register(r'days',        views.DayViewSet)
router.register(r'plans',       views.PlanViewSet)
router.register(r'users',       views.UserViewSet)

from django import template
from accounts.models import Profile


# Creates a registry for this custom template tags
register = template.Library()

# This decorator registers the function as a template tag
@register.simple_tag(takes_context=True)
def is_subscribe(context):
    request = context['request']
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            return profile.is_subscribed
        except Profile.DoesNotExist:
            return False
    return False
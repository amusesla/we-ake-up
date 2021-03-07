from django.views      import View
from django.http       import JsonResponse


from django.core.cache import cache
from django_redis import get_redis_connection

class LoginView(View):
    def get(self, request):
        if cache.get('foo'):
            obj = {
                    'foo': cache.get('foo'),
                    'expire_in': cache.ttl('foo'),
                    }
            return JsonResponse({'message':obj})
        else:
            return JsonResponse({'message':'does not exsit'})

    def post(self, request):
        obj = {
                'user_session': '213412312',
                'user_id':'amusesla'
                }

        cache.set('foo', obj, timeout=20)

        return JsonResponse({'message': 'success'})

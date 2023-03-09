def custom_admin_middleware(get_response):

    def middleware(request):
        print(request.user)
        # print('before response')
        response = get_response(request)
        # print('After response')

        return response

    return middleware
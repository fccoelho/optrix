requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        'optrix': '../optrix',
        'data': '../data/'
    }
});

requirejs(['optrix/main']);

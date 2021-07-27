import Service from '@/services/base';


const savedCartService = new Service('savedCart');


savedCartService.registerFunction('share', {
    url: '/api/me/carts/<savedCartId>/share/',
    method: 'post',
    urlVariables: ['savedCartId']
});

savedCartService.registerFunction('delete', {
    url: '/api/me/carts/<savedCartId>/',
    method: 'delete',
    urlVariables: ['savedCartId']
});


export default savedCartService;
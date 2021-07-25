import Service from '@/services/base';


const savedCartService = new Service('savedCart');


savedCartService.registerFunction('share', {
    url: '/api/carts/<savedCartId>/share/',
    method: 'post',
    urlVariables: ['savedCartId']
});

export default savedCartService;
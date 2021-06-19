import Alert from "@/alert";
import apiClient from "@/api";


function Service (name) {
    this.name = name;
};

Service.prototype.register_function = function (name, config) {
    const { url, 
            method, 
            successMsg, 
            errorMsg } = config;


    function serviceFunction (
        data,
        successCallback = () => null,
        errorCallback = () => null) {

        return apiClient[method](url, data)
            .then(res => {
                successMsg ? Alert.success(successMsg) : null;

                successCallback(res);
            })
            .catch(err => {
                const errResponseStatus = err.status;

                const badRequestErr = errResponseStatus === 400;
                
                if (!badRequestErr) return;
                
                errorCallback(err);

                errorMsg ? Alert.info(errorMsg) : null;
            })
    }

    Object.defineProperty(
        this, 
        name,
        {
            writable: false,
            enumerable: false,
            configurable: false,
            value: serviceFunction
        } 
    )  
};

export default Service;
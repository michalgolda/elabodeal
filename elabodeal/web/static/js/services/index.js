import Alert from "@/alert";
import apiClient from "@/api";


function Service (name) {
    this.name = name;
};

Service.prototype.register_function = function (name, config) {
    var { url, 
          method, 
          successMsg, 
          errorMsg } = config;


    function serviceFunction (
        data,
        { successCallback, 
          errorCallback, 
          hideDefaultSuccessMsg, 
          hideDefaultErrorMsg } = {}) {

        successMsg = !hideDefaultSuccessMsg ? successMsg : null;
        errorMsg = !hideDefaultErrorMsg ? errorMsg : null;

        return apiClient[method](url, data)
            .then(res => {
                successMsg ? Alert.success(successMsg) : null;

                if (successCallback) successCallback(res);
            })
            .catch(err => {
                const errResponseStatus = err.status;

                const badRequestErr = errResponseStatus === 400;
                
                if (!badRequestErr) return;
                
                if (errorCallback) errorCallback(err);

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
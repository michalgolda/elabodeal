import Alert from "@/alert";
import apiClient from "@/api";


function Service (name) {
    this.name = name;
}

Service.prototype.prepareURL = function (url, urlVariables, data) {
    urlVariables.map((urlVariableName) => {
        const urlVariableValue = data.get(urlVariableName);

        if (!urlVariableValue)
            throw new Error(`data object does not contain a ${urlVariableName} field`);

        const preparedURL = url.replace(`<${urlVariableName}>`, urlVariableValue);

        if (!preparedURL)
            throw new Error(`url string does not contain a ${urlVariableName} variable`);

        url = preparedURL;
    });

    return url;
};


Service.prototype.registerFunction = function (functionName, config) {
    var { url, 
          method,
          urlVariables,
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
        url = urlVariables ? this.prepareURL(url, urlVariables, data) : url;

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
        functionName,
        {
            writable: false,
            enumerable: false,
            configurable: false,
            value: serviceFunction
        } 
    )  
};

export default Service;
import axios from "axios";

const request = {
  install(Vue) {
    Vue.prototype.$request = async (request, path, data, options) => {
      var headers = options || { "Content-Type": "application/json" };
      //console.log(process.env.API_URL);
      return makeRequest(request, path, data, headers);
    };
  },
};

function makeRequest(request, path, data, headers) {
  switch (request) {
    case "get":
      return axios.get("http://localhost:5000/" + path, {
        headers: headers,
      });
    case "post":
      return axios.post("http://localhost:5000/" + path, data, {
        headers: headers,
      });
    case "put":
      return axios.put("http://localhost:5000/"  + path, data, {
        headers: headers,
      });
    case "delete":
      return axios.delete("http://localhost:5000/" + path, data, {
        headers: headers,
      });
    default:
      return "request type unknown";
  }
}

export default request;
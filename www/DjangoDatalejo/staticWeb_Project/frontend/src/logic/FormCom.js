import axios from "axios";
import Cookies from "js-cookie";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const ENDPOINT_PATH = "http://localhost:8000/Contacto/";

export default {
    setMyCookie(cookie) {
      Cookies.set("aCookie", cookie);
    },
    getMyCookie() {
      return Cookies.get("aCookie");
    },
  comForm() {
    //var csrftoken = Cookies.get('X-CSRFTOKEN');
    const myform = getMyCookie();
    console.log(myform)
    console.log('datos saliendo por axios')
    return axios.post(ENDPOINT_PATH,myform)
    /*axios({
      method: post, 
      url:ENDPOINT_PATH, 
      data:myform,
      //responseType: 'X-CSRFTOKEN',
      //{
      headers: {
           'X-CSRFTOKEN': csrfCookie,
       },
      //},
      });*/
  },
};
<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/contacto0.jpg') + ')' }"
            style="z-index: -1;">
                <navbar_dl></navbar_dl>
            <div class="container2fm" >
                <h1 class="contact-title">{{tituloArticulo}}</h1>
            </div>
        </section>
        <section >
            <div class="row " :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }" 
                style="z-index: -1;">
                <div class="col-md-3">
                </div>
                <div class="col-md-6"  >
                     <!--<div class="frame-fm" :style= "{ backgroundImage: 'url(' + require('@/assets/contact1.jpg') + ')' }" >
                       <b-form @submit="onSubmit" method="post"  v-if="show">
                        <b-form-group
                            id="input-group-1"
                            label="Correo Electrónico"
                            label-for="input-1"
                        >
                        <b-form-input
                            id="input-1"
                            v-model="form.email"
                            type="email"
                            required
                            placeholder="Ingresa tu correo electrónico"
                            ></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label="Tu nombre:" label-for="input-2">
                            <b-form-input
                            id="input-2"
                            v-model="form.name"
                            required
                            placeholder="Ingresa tu Nombre"
                            ></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-3" label="Dejanos tu mensaje:" label-for="input-3">
                            <b-form-input
                            id="input-3"
                            v-model="form.msg"
                            required
                            placeholder="Tu consulta o requerimiento"
                            ></b-form-input>
                        </b-form-group>

                        <b-button type="submit" >Submit</b-button>
                        </b-form>

                    </div>-->
                    <div  style="padding: 25px;">
                    <h1><br><br><br>Solicite mas información</h1>
                    <h2><br>Póngase en contacto con nosotros para obtener mas información adicional sobre los productos y servicios datalejo</h2>
                    <h3><br>
                        <h3>Teléfono:     +57 3183694687     <br></h3>
                        <h3>Correo:<a href="mailto:contactodatalejo@gmail.com"> contactodatalejo@gmail.com </a></h3>
                    </h3>
                    <h2><br>Horario de atención: Lunes a Viernes de 8:00am a 6:00pm</h2>
                    </div>
                    <form class="formex" method="post"  @submit="checkForm"   novalidate="false"
                        style="z-index: -1;"> > <!-- quitar para mostrar el formulario-->
                        <h3 class="pex">{{rta}}</h3>
                         <p v-if="errors.length">
                            <b>Por favor, corrija el(los) siguiente(s) error(es):</b>
                            <ul>
                                <li v-for ="error in errors">{{ error }}</li>
                            </ul>
                        </p>
                        <!--{% csrf_token %}-->
                        <!--<input type="hidden" name="_token" v-bind:value="csrf">-->
                        <h2 class="h2ex">ESCRIBENOS</h2>
                            <div >
                                <p class="pex" type="Nombre:">
                                    <input
                                        id="name"
                                        name="name" 
                                        type="text"
                                        v-model="name" 
                                        placeholder="Escribe tu nombre.."                                    
                                    > 
                                </p>
                            </div>
                            <div >
                                <p class="pex" type="Email:">
                                    <input
                                        id="email"
                                        name="email" 
                                        type="text" 
                                        v-model="email"
                                        placeholder="Dejanos tu correo electrónico.."
                                    > 
                                </p>
                            </div>
                            <div >
                                <p class="pex" type="Mensaje:">
                                    <input 
                                        id="msg"
                                        name="msg" 
                                        type="text" 
                                        v-model="msg" 
                                        placeholder="Escribe tu mensaje.."
                                    >
                                </p>
                            </div>
                            <button type="submit">Enviar </button>
                        <div class="mydiv">
                            <span class="myfieldPhone"></span>+57 3183694687
                            <span class="myfieldMail"></span> <a href="mailto:contactodatalejo@gmail.com">contactodatalejo@gmail.com</a>
                        </div>
                        </form>
                <div class="col-md-3">
                </div>
                </div>
            </div>
        </section >
        <lowerBanner />
    </div>
</template>

<script>
import axios from 'axios';
//import Parallax from "vue-parallaxy";
import navbar_dl from '@/components/page_web/ListNavbar.vue';
import articuloFrame from '@/components/ArticuloFrame/ArticuloFrame.vue';
import articuloIzqFrame from '@/components/ArticuloFrame/ArticuloIzqFrame.vue';
import articuloIzqFrameColor from '@/components/ArticuloFrame/ArticuloIzqFrameColor.vue';
import lowerBanner from '@/components/ArticuloFrame/LowerBanner.vue';
import articuloImaTresCols from '@/components/ArticuloFrame/ArticuloImaTresCols.vue';
import FormCom from "@/logic/FormCom";
//const csrftoken = Cookies.get('csrftoken');
export default {
  name: 'paralax_dl',
  components: {
    navbar_dl,
    articuloIzqFrame,
    articuloFrame,
    articuloImaTresCols,
    lowerBanner,
  },
  props: {
      
    tituloArticulo:{
        type: String,
        default:"CONTACTO"
    },
  },
  data(){
    return {        
        //csrfmiddlewaretoken: '',    
        email: '',
        name: '',
        msg:'',
        rta:'',
        errors: [],
      //title0:'¿Necesitas saber donde poner tu negocio? Nosotros te ayudamos.',
    }    
  },
 methods: {    
     checkForm: function (e) {      
        this.errors = [];
        if (!this.name) {
            this.errors.push("El nombre es obligatorio.");
        }
        if (!this.msg) {
            this.errors.push("Por favor deje un mensaje.");
        }
        if (!this.email) {
            this.errors.push('El correo electrónico es obligatorio.');
        } else if (!this.validEmail(this.email)) {
            this.errors.push('El correo electrónico debe ser válido.');
        }
        //console.log(this.errors.length)
        if (this.errors.length>0) {
            //return true;
            console.log('tenemos errores');
        }
        else
        {
            const cookie={'name':this.name,'email':this.email,'msg':this.msg};
            FormCom.setMyCookie(cookie);
            FormCom.comForm(cookie);
            console.log('entramos a post'); 
            this.rta="Datos Enviados! Muchas gracias ";
        }
        e.preventDefault();
    },
    validEmail: function (email) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    },
    /*postNow() {
        
        axios({
            method:"post",
            url: 'http:localhost:8000/Contacto/', 
            data : {
                name: this.name,
                email: this.email,
                msg: this.msg
            }, // the data to post
            headers: {
                //'Content-type': 'application/x-www-form-urlencoded',
                //"X-CSRFToken" : this.csrfmiddlewaretoken,
                "X-CSRFToken" :  csrftoken 
            }       
        }).then(function (response) {
            console.log(response.data)
            this.rta="Gracias, te responderemos lo antes posible."
        }).catch(function (error) {
            console.log(error.response)
            this.rta="error, no fue posible enviar."
        })

       // axios.post('http://localhost:8000/Contacto/', this.form)
    }*/
 },
/*
    mounted: function(){
      this.csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
    }*/
};
</script>
<style >
/*
@import "assets/fonts/FoundryGridnik-Medium.otf";
.sencore-title{
    font-family: 'FoundryGridnik';
}*/
.row
{
    z-index: -1;
}
.header {
    color: #36A0FF;
    font-size: 27px;
    padding: 10px;
}
/*
.bigicon {
    font-size: 35px;
    color: #36A0FF;
}
*/

.framle {
  font-family: FoundryGridnik;
  font-style: normal;
  color: #42b983;
  font-size: 56px;
}

.container2fm{
    height: 40vh;
    text-align: center;
    vertical-align: middle;
    font-weight: bold;
    padding: 10rem 0rem 0rem 0rem;
}
.fondo1{
    /*background: url(imagen.png) no-repeat center center fixed;*/
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    /*opacity:0.2;*/
}
.contact-title{
    color: rgb(221, 225, 236);
    /*color: RGB(27,34,44);*/
    font-size: 2.8vw;
    /*font-size: 320%;*/
    text-shadow: -0.2px -0.2px  rgb(173, 173, 173), 0.2px -0.2px  rgb(173, 173, 173), -0.2px 0.2px  rgb(173, 173, 173),-0.2px 0.2px  rgb(173, 173, 173); 
    size: 40vh;
    /*background: rgba(0, 0, 0, 0.6);*/
}

@media only screen and (max-width: 800) { 

 .contact-title{
     font-size: 8vw;
 }
}
.frame-fm{

    height: 50vh;
    padding: 40px;
}
.navbar_dl{
        color: white;
}
bodyex{
    background:#59ABE3;
    margin:0
    }
.formex{
    width:340px;
    height:440px;
    background:#e6e6e6;
    border-radius:8px;
    box-shadow:0 0 40px -10px #000;
    margin:calc(50vh - 220px) auto;
    padding:20px 30px;
    max-width:calc(100vw - 40px);
    box-sizing:border-box;
    font-family:'Montserrat',sans-serif;
    position:relative
    }
.h2ex{
    margin:10px 0;
    padding-bottom:10px;
    width:180px;
    color:#78788c;
    border-bottom:3px solid #78788c
    }
input{
    width:100%;
    padding:10px;
    box-sizing:border-box;
    background:none;
    outline:none;
    resize:none;
    border:0;
    font-family:'Montserrat',sans-serif;
    transition:all .3s;
    border-bottom:2px solid #bebed2
    }
input:focus{
    border-bottom:2px solid #78788c
    }
.pex:before{
    content:attr(type);
    display:block;
    margin:28px 0 0;
    font-size:14px;
    color:#5a5a5a
    }
button{
    float:right;
    padding:8px 12px;
    margin:8px 0 0;
    font-family:'Montserrat',sans-serif;
    border:2px solid #78788c;
    background:0;
    color:#5a5a6e;
    cursor:pointer;
    transition:all .3s}
button:hover{
    background:#78788c;
    color:#fff
    }
.mydiv{
    content:'Hi';
    position:absolute;
    bottom:-15px;right:-20px;
    background:#50505a;
    color:#fff;
    width:355px;
    padding:16px 4px 16px 0;
    border-radius:6px;
    font-size:13px;
    box-shadow:10px 10px 40px -14px #000}
.myfieldEmail{
    margin:0 5px 0 15px}
.myfieldPhone{
    margin:0 5px 0 15px}

a:link
{
text-decoration:none;
  /*color: rgb(225, 232, 241);*/
  color: rgb(7, 109, 211);
}

</style>

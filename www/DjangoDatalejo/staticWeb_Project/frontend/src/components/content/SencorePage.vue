<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/sencore0.jpg') + ')' }">
                <navbar_dl></navbar_dl>
            <div class="container2" >
                <h1 class="sencore-title">{{tituloArticulo}}</h1>
            </div>
        </section>
        <section :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
            <div class="container1" >
            </div>
        </section>
        
        <div class="frame-classic">
        <articuloFrame  
            v-bind:tituloArticulo= "title3" 
            v-bind:textoArticulo= "article3" 
            v-bind:textoSobreImagen= "textimg3"
            v-bind:imagenConGamma= "imagenConGamma3"
            v-bind:imagenFondo= "imagenFondo3"
        />
        </div>
        <div class="frame-classic">
            <articuloIzqFrame  
                v-bind:tituloArticulo= "title0" 
                v-bind:textoArticulo= "article0" 
                v-bind:textoSobreImagen= "textimg0"
                v-bind:imagenConGamma= "imagenConGamma0"
                v-bind:imagenFondo= "imagenFondo0"
            />
        </div>

        <div class="frame-classic">
        <articuloFrame  
            v-bind:tituloArticulo= "title1" 
            v-bind:textoArticulo= "article1" 
            v-bind:textoSobreImagen= "textimg1"
            v-bind:imagenConGamma= "imagenConGamma1"
            v-bind:imagenFondo= "imagenFondo1"
        />
        </div>
        <lowerBanner />
    </div>
</template>

<script>
//import Parallax from "vue-parallaxy";
import navbar_dl from '@/components/page_web/ListNavbar.vue';
import articuloFrame from '@/components/ArticuloFrame/ArticuloFrame.vue';
import articuloIzqFrame from '@/components/ArticuloFrame/ArticuloIzqFrame.vue';
import articuloIzqFrameColor from '@/components/ArticuloFrame/ArticuloIzqFrameColor.vue';
import lowerBanner from '@/components/ArticuloFrame/LowerBanner.vue';
export default {
  name: 'paralax_dl',
  components: {
    navbar_dl,
    articuloIzqFrame,
    articuloFrame,
    lowerBanner
  },
  props: {
      tituloArticulo:{
        type: String,
        default:"SENCORE"
      },
  },
  data(){
    return {    
        
      title3:'Sensores a la medida',
      article3:'El servicio  Sencore es una solución '+
                'basada en sensores y desarrollo de hardware que permite capturar y analizar información'+
                ',generar alarmas e indicadores de acuerdo a la necesidad de su negocio.'+
                'Desarrollamos sensores de temperatura, proximidad, profundidad, entre otros. Transformamos sus datos en información.',
      textimg3: 'Sencore',
      imagenConGamma3:"Servicios.png",
      imagenFondo3:"sencore5.jpg",

      title0:'¿Cómo es el proceso?',
      article0:'Evaluamos el requerimiento que nos haga llegar de manera escrita, luego  establecemos  reuniones virtuales y de ser necesario visitas a campo. Esto nos permitirá entender mejor sus necesidad. '+
                'Presentamos una propuesta tecnológica y económica que cumpla el requerimiento solicitado '+
                'buscando siempre, el menor precio, '+
                'ahorro energético y calidad. '+
                'Contamos con un equipo de ingenieros electrónicos y científicos de datos altamente calificados para garantizar la captura y el análisis de sus datos. ',
      textimg0: 'Sencore',
      imagenConGamma0:"Servicios.png",
      imagenFondo0:"raspis.jpg",


      title1:'¿ Y Después?',
      article1:'Generamos un piloto a su medida estableciento las funciones minímas de operación. En esta estapa se captura la retroalimentción por parte del cliente. '+
                'Una vez superada la fase de retro alimentación se establecen los plazos de entrega y comienza el desarrollo. '+ 
                'Finalemente, entregamos la solución tecnológica para mejorar su proceso. ',
      textimg1: 'Sencore',
      imagenConGamma1:"quehacemos.png",
      imagenFondo1:"Sencore3.jpg",
    }
  },
 
};
</script>
<style>


.container2{
    height: 35vh;
    text-align: center;
    vertical-align: middle;
    font-weight: bold;
    padding: 10rem 0rem 0rem 0rem ;
}
.fondo1{
    /*background: url(imagen.png) no-repeat center center fixed;*/
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    /*opacity:0.2;*/
}
.sencore-title{
    /*color: rgb(221, 225, 236);*/
    /*color: RGB(27,34,44);
    color: #05668d;
    color: #028090;
    color: #2b2d42;
    color: #8d99ae;*/
    color: #edf2f4; 
    /*color: #02c39a;*/
    font-size: 2.8vw;
    /*font-size: 320%;*/
    text-shadow: -0.2px -0.2px  rgb(173, 173, 173), 0.2px -0.2px  rgb(173, 173, 173), -0.2px 0.2px  rgb(173, 173, 173),-0.2px 0.2px  rgb(173, 173, 173); 
    size: 40vh;
    /*background: rgba(0, 0, 0, 0.6);*/
}

.navbar_dl{
        color: white;
}

.color_item{
  color: rgb(172, 172, 184);
}

@media only screen and (max-width: 800) { 

 .sencore-title{
     font-size: 8vw;
 }
}
</style>

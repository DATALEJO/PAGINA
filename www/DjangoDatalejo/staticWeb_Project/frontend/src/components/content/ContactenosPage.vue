<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/plan-1859394_1920.jpg') + ')' }">
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
        <div class="frame-classic-shortcp">
            <section :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">  
                <div class="container2" >
                    <h1 ><br><br>{{tituloArticulo1}}<br><br></h1>
                    <h2 >{{textoArticulo1}}</h2>
                </div>
            </section>
        </div>
        <div class="frame-classic">
            <articuloIzqFrame  
                v-bind:tituloArticulo= "title2" 
                v-bind:textoArticulo= "article2" 
                v-bind:textoSobreImagen= "textimg2"
                v-bind:imagenConGamma= "imagenConGamma2"
                v-bind:imagenFondo= "imagenFondo2"
            />
        </div>     
        <div class="frame-classic-shortcp">
            <section :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">  
                <div class="container2" >
                    <h1 >{{tituloArticulo2}}<br><br></h1>
                    <h2 >{{textoArticulo2}}</h2>
                </div>
            </section>
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
        default:"Nosotros "
      },
      tituloArticulo1:{
        type: String,
        default:"Misión "
      },
      textoArticulo1:{
        type: String,
        default:'Proveer soluciones tecnológicas basadas en el uso de sensores'+
                ', herramientas iot, algoritmos de aprendizaje y  análisis de '+
                'datos orientadas a la toma de decisiones para optimizar recursos'+
                '. Nuestra promesa de valor es la velocidad de los procesos y la '+
                'visualización de los análisis. ',
      },
      tituloArticulo2:{
        type: String,
        default:"Visión "
      },
      textoArticulo2:{
        type: String,
        default:'Acercar a  nuestros clientes a nuevas tecnologías que les permitan '+
                'mejorar sus procesos y  de esta manera  posicionarnos como un '+
                'referente tecnológico dentro de la región.',
      }
  },
  data(){
    return {     
      title0:'Nosotros',
      article0:'Datalejo desarrolla soluciones tecnológicas diseñadas '+
                'para la captura, el procesamiento y el análisis de datos '+
                'haciendo uso de  imágenes o variables de su entorno capturadas '+
                'por nuestros sensores.',
      textimg0: 'Nosotros',
      imagenConGamma0:"Servicios.png",
      imagenFondo0:"contactenos1.jpg",


      title1:' ',
      article1:'Entendemos que muchas veces se carece de información para tomar decisiones '+
              'o esta información no está a su alcance de forma inmediata. Para solucionar '+
              'esto usamos sensores, iot  y algoritmos de aprendizaje automático que'+
              ' permiten obtener la información para que se puedan tomar las decisiones '+
              'lo más rápido posible. ',

      textimg1: 'contactenos',
      imagenConGamma1:"quehacemos.png",
      imagenFondo1:"contactenos2.jpg",


      title2:' ',
      article2:'En otras ocasiones no se tiene las herramientas para hacer seguimiento a '+
                'cada paso de su proceso o este es demasiado engorroso; por lo que nuestros '+
                'productos y servicios permiten medir y aumentar la velocidad en los procesos',

      textimg2: 'contactenos',
      imagenConGamma2:"quehacemos.png",
      imagenFondo2:"contactenos3.jpg",
    }
  },
 
};
</script>
<style>
.frame-classic-shortcp{
    height: 100vh;

}

.container2{
    height: 70vh;
    text-align: center;
    vertical-align: middle;
    font-weight: bold;
    padding: 12rem ;
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
    color: rgb(221, 225, 236);
    size: 40vh;
    background: rgba(0, 0, 0, 0.6);
}
</style>

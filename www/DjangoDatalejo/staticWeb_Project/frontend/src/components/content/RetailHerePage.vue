<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/retailHere0.jpg') + ')' }">
                <navbar_dl></navbar_dl>
            <div class="container2" >
                <h1 class="retailhere-title">{{tituloArticulo}}</h1>
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
        <div class="frame-classic">
            <articuloImaTresCols  
                v-bind:imagenConGamma= "imagenConGamma2" 
                v-bind:tituloSubArticuloA= "tituloSubArticuloA0" 
                v-bind:textoSubArticuloA= "textoSubArticuloA0"
                v-bind:textoSubArticuloB= "textoSubArticuloB0"
                v-bind:textoSubArticuloC= "textoSubArticuloC0"
                v-bind:imagenSubArticuloA= "imagenSubArticuloA0"
                v-bind:imagenSubArticuloB= "imagenSubArticuloB0"
                v-bind:imagenSubArticuloC= "imagenSubArticuloC0"
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
import articuloImaTresCols from '@/components/ArticuloFrame/ArticuloImaTresCols.vue';
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
        default:"RETAILHERE"
      },
  },
  data(){
    return {     
      title0:'¿Necesitas saber donde poner tu negocio? Nosotros te ayudamos.',
      article0:'Ubicamos geográficamente su negocio en el punto donde tendrá más'+
               ' impacto y mejores ventas  de acuerdo al análisis de variables espaciales.',
      textimg0: 'RetailHere',
      imagenConGamma0:"Servicios.png",
      imagenFondo0:"retailHere1.jpg",


      title1:'¿Cómo lo hacemos?',
      article1:'Por medio del análisis de variables espaciales y económicas '+
                'creamos un modelo que permite detectar el mejor sitio para el '+
                'negocio que se quiere ubicar.  ',
      textimg1: 'RetailHere',
      imagenConGamma1:"quehacemos.png",
      imagenFondo1:"retailHere2.jpg",


      tituloSubArticuloA0: 'Así usted tendrá:' ,
      textoSubArticuloA0: 'Mejor visibilidad por parte de su clientes.',
      textoSubArticuloB0: 'Distribución geográfica óptima para sus tiendas o centros de producción.',
      textoSubArticuloC0: 'Aumento en posibilidades de venta.',
      imagenConGamma2: "retailHere3.jpg" ,
      imagenSubArticuloA0:"eye.png",
      imagenSubArticuloB0:"location.png",
      imagenSubArticuloC0:"buy.png",
    }
  },
 
};
</script>
<style >
/*
@import "assets/fonts/FoundryGridnik-Medium.otf";
.sencore-title{
    font-family: 'FoundryGridnik';
}*/



.container2{
    height: 35hv;
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
.retailhere-title{
    /*color: rgb(221, 225, 236);*/
    /*color: RGB(27,34,44);
    color: #05668d;
    color: #028090;
    color: #2b2d42;
    color: #8d99ae;
    color: #edf2f4;*/
    color: #02c39a;
    font-size: 320%;
    text-shadow: -0.2px -0.2px  rgb(173, 173, 173), 0.2px -0.2px  rgb(173, 173, 173), -0.2px 0.2px  rgb(173, 173, 173),-0.2px 0.2px  rgb(173, 173, 173); 
    size: 40vh;
    /*background: rgba(0, 0, 0, 0.6);*/
}
.navbar_dl{
        color: white;
}


</style>

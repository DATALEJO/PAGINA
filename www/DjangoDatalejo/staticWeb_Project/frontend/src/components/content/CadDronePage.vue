<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/capdron0.jpg') + ')' }">
                <navbar_dl></navbar_dl>
            <div class="container2" >
                <h1 class="caddrone-title">{{tituloArticulo}}</h1>
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
        default:"CADDRONE"
      },
  },
  data(){
    return {     
      title0:'Usamos drones para generar modelos 3d de su estructura.',
      article0:'Da ventajas como,'+
                'Seguridad, '+
                'Privacidad y   '+
                'Seguridad Sanitaria',
      textimg0: 'Capdron',
      imagenConGamma0:"Servicios.png",
      imagenFondo0:"capdron1.jpg",


      title1:'Usos',
      article1:'Ayuda visual para de venta inmuebles. \n'+
                'Seguimiento de obra.\n'+
                'Calculo de volúmenes.\n'+
                'Muestra visual para guías turísticas.\n'+
                'Evaluación estado de maquinaria y equipo.\n',

      textimg1: 'Capdron',
      imagenConGamma1:"quehacemos.png",
      imagenFondo1:"capdron2.jpg",
    }
  },
 
};
</script>
<style>


.container2{
    height: 35vh;
    text-align: center;
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
.caddrone-title{
    /*color: rgb(221, 225, 236);*/
    /*position: absolute;
    text-align: center;*/
    color: RGB(27,34,44);
    font-size: 320%;
    text-shadow: -0.2px -0.2px  rgb(173, 173, 173), 0.2px -0.2px  rgb(173, 173, 173), -0.2px 0.2px  rgb(173, 173, 173),-0.2px 0.2px  rgb(173, 173, 173); 
    size: 40vh;
    /*top:12rem;*/
    /*background: rgba(0, 0, 0, 0.6);*/
}
</style>

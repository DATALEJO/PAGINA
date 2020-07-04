<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/droneFacade0.png') + ')' }">
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
        default:"Análisis de fachadas"
      },
  },
  data(){
    return {     
      title0:'Análisis de Fachadas.',
      article0:'Por medio de uso de drones, aprendizaje automático y '+
               'sensores analizamos sus fachadas para encontrar defectos.'+
               ' Esta tecnología también permite clasificar y contar objetos.',
      textimg0: 'DronFacade',
      imagenConGamma0:"Servicios.png",
      imagenFondo0:"droneFacade1.png",


      title1:'Usos',
      article1:'Encontrar humedad, fisuras, daños en acabados'+
               ', modelo de referencia para restauración y control '+
               ' de fachadas, revisión de áreas comunes.',
                /*Ayuda visual para de venta inmuebles. '+
                'Seguimiento de obra. '+
                'Calculo de volúmenes. '+
                'Muestra visual para guías turísticas. '+
                'Evaluación estado de maquinaria y equipo.',*/

      textimg1: 'DronFacade',
      imagenConGamma1:"Usos.png",
      imagenFondo1:"droneFacade2.png",
    }
  },
 
};
</script>
<style>

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

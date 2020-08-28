<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/droneFacade0.png') + ')' }">
                <navbar_dl></navbar_dl>
            <div class="container2" >
                <h1 class="dronefacade-title">{{tituloArticulo}}</h1>
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
        default:"DRONE FACADE"
      },
  },
  data(){
    return {     
      title0:'Análisis de Fachadas.',
      article0:'Por medio de uso de drones, aprendizaje automático y '+
               'sensores analizamos sus fachadas para encontrar defectos.'+
               ' Esta tecnología también permite clasificar y contar objetos.\n'+
               ' Las inspecciones pueden realizarse rápidamente y bajo demanda con imágenes en vivo, precisas y '+
                'de alta resolución transmitidas de inmediato para la evaluación y la toma de decisiones dentro y '+
                'fuera del sitio. El monitoreo crítico y preventivo del estrés de la infraestructura se puede llevar a '+
                'cabo de manera regular con un gran ahorro de costos y protección para la vida humana.',

      textimg0: 'DronFacade',
      imagenConGamma0:"Servicios.png",
      imagenFondo0:"droneFacade1.png",


      title1:'Usos',
      article1:'Encontrar humedad, fisuras, daños en acabados '+
               ',modelo de referencia para restauración y control '+
               ' de fachadas, revisión de áreas comunes.\n '+
                '\n Infraestructura en la industria energética:\n • Paneles solares.\n •  turbinas eólicas.\n •  líneas eléctricas.'+
                '\n\n  Infraestructura de transporte:\n •  Carreteras\n •  túneles\n •  canales\n •  puentes\n •  puertos\n •  aeropuertos.'+
                '\n\n  Infraestructura de comunicaciones:\n •  Torres para telefonía celular\n •  instalaciones de cable de '+
                'fibra óptica. '+
                '\n\n Estructuras:\n • Edificios\n •  plantas\n •  tejados\n •  fachadas.',
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
    height: 35vh;
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
}.dronefacade-title{
    /*color: rgb(221, 225, 236);*/
    color: RGB(27,34,44);
    font-size: 2.8vw;
    /*font-size: 320%;*/
    text-shadow: -0.2px -0.2px  rgb(173, 173, 173), 0.2px -0.2px  rgb(173, 173, 173), -0.2px 0.2px  rgb(173, 173, 173),-0.2px 0.2px  rgb(173, 173, 173); 
    size: 40vh;
    text-align: center;
    /*background: rgba(0, 0, 0, 0.6);*/
}

@media only screen and (max-width: 800) { 

 .dronefacade-title{
     font-size: 8vw;
 }
}
</style>

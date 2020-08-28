<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/mapsafe0.jpg') + ')' }">
                <navbar_dl></navbar_dl>
            <div class="container2" >
                <h1 class="mapsafe-title">{{tituloArticulo}}</h1>
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
        default:"MAPSAFE"
      },
  },
  data(){
    return {     
      title0:'Te ayudamos a localizar zonas inseguras',
      article0:'Usamos diferentes fuentes compiladas de internet y '+ 
                'entidades estatales para cartografiar zonas inseguras dentro '+
                'de las principales ciudades del país. Realizamos visitas a campo '+
                'siempre que sea posible, con el fin de determinar la veracidad de la '+
                'información colectada, esto permite re afirmar la veracidad de las zonas inseguras encontradas.',
      textimg0: 'MapSafe',
      imagenConGamma0:"Servicios.png",
      imagenFondo0:"mapsafe1.jpg",


      title1:'Usos',
      article1:'Permite determinar rutas seguras por donde se podrían realizar recorridos y/o entregas.'+
                'Por medio de este producto se puede implementar protocolos de seguridad y así mitigar riesgos.',

      textimg1: 'Capdron',
      imagenConGamma1:"Usos.png",
      imagenFondo1:"mapsafe2.jpg",
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
.mapsafe-title{
    color: rgb(221, 225, 236);
    /*color: RGB(27,34,44);*/
    font-size: 2.8vw;
    /*font-size: 320%;*/
    text-shadow: -0.2px -0.2px  rgb(173, 173, 173), 0.2px -0.2px  rgb(173, 173, 173), -0.2px 0.2px  rgb(173, 173, 173),-0.2px 0.2px  rgb(173, 173, 173); 
    size: 40vh;
    /*background: rgba(0, 0, 0, 0.6);*/
}

@media only screen and (max-width: 800) { 

 .mapsafe-title{
     font-size: 8vw;
 }
}
</style>

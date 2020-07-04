<template>
    <div class="ParalaxVue">
        <div>
          <navbar_dl> </navbar_dl>
        </div>
        <div class="parallax-container">
          <parallax  class="frame_principal" direction='down' >
            <img :src="require('@/assets/topBanner2.png')" alt="back" >
          </parallax>
          <parallax :direction="down" speed-factor="0.5" class="frame_secundario">
            <container  >
              <h1 class="parallax-title">{{titulo}}<br></h1>
              <div class="mx-auto">
                  <h2 style="text-align:center;" class="parallax-eslogan">{{eslogan}}</h2>
              </div>
            </container>
            <img  :src="require('@/assets/topBanner1.png')" alt="middle"   >
          </parallax>
          <parallax  class="frame_terciario" direction='up'>
            <img  :src="require('@/assets/topBanner0.png')" alt="front"   >
          </parallax>
        </div>
    </div>
</template>

<script>
import Parallax from "vue-parallaxy";
import navbar_dl from '@/components/page_web/ListNavbar.vue';
export default {
  name: 'paralax_dl',
  components: {
    Parallax,
    navbar_dl
  },
  props: {
      titulo:{
        type: String,
        default:"Soluciones IOT"
      },
      eslogan:{
        type: String,
        default:"Captura y análisis de datos con drones  y sensores en la era 4.0"
      },
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

ul {
  list-style-type: none;
  padding: 0;
}

.parallax-container {
  position: relative;
  height: 105vh;
  -webkit-perspective: 1px;
          perspective: 1px;
  z-index: -1;
}
.frame_principal{
  position: absolute;
  /*speed-factor:"0.5";*/
  /*direction:'down';*/
  /*sectionHeight: "170";*/
  top: 0;
  left: 0;
  width: 100%;
  z-index: -1;
  /*height:"1600px";*/
}

.frame_secundario{
  position: absolute;
  /*direction:'up';*/
  top: 0;
  left: 0;
  width: 100%;
  z-index: -1;
  /*height:"1600";*/
}
.parallax-title {
  position: absolute;
  top: 27%;
  left: 0;
  right: 0;
  padding: 20px;
  /*background: rgba(0, 0, 0, 0.6);*/
  color: black;
  text-align: center;
}


.parallax-eslogan {
  position: absolute;
  top: 36%;
  left: 38%;
  right: 0;
  width: 25%;
  /*padding: 20px;*/
  /*background: rgba(0, 0, 0, 0.6);*/
  color: rgb(98, 187, 188);
  text-align: center;
  border: 2px rgb(98, 187, 188) solid;
  border-radius: 10px;
  border-spacing: 50px;
  padding: 3px 20px 3px 20px;
  font-size: medium;

}

@media only screen and (max-width: 600px) {  
  .parallax-eslogan {
    left: 0;
    top: 25%;
    width: 100%;
  }
  .parallax-title {
    top: 15%;
  }
}
.big-row {
  height: 30vh;
}
.ParalaxVue{
  z-index: -1;
}
</style>
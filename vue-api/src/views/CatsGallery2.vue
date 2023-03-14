<template>
  <div>
    <Header/>
    <div class="row">
      <table class="table">
        <thead>
          <tr>
            <th class="text-center">GATOS DEL MUNDO</th>
          </tr>
        </thead>
      <div v-for="(cat, index) in cat_info" :key="index" class="col-md-4">
        <tbody class="table-body">
          <tr class="table-row">
            <td ><img :src="cat.url" alt="gatito" class="card-img-top table-img"></td>
          </tr>
          <tr>
            <td class="text-center">{{cat.name}}</td>
          </tr>
        </tbody>
      </div>
      <BreakLine/>
     </table>
    </div>

    <ScrollToTop/>
    <PagesFooter/>
  </div>
</template>

<style scoped>
.row{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.card {
  margin: 1rem;
  display: flex;
  border-color: #CE7204;
}

.card-img-top{
  height: 300px;
  object-fit: contain;
}
.table-body {
display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.table-row{
  display: flex;
  flex-direction: row;
}

.table-img {
  height: 400px;
  width: 600px;
  object-fit: contain;
}




</style>

<script>
import { getApi } from "@/axios-api";
import PagesFooter from "@/components/PagesFooter.vue";
import ScrollToTop from "@/components/ScrollToTop.vue";
import Header from "@/components/Header.vue";
import BreakLine from "../components/BreakLine.vue";

export default {
  components: {
    PagesFooter,
    ScrollToTop,
    Header,
    BreakLine,
  },
  data() {
    return {
      urls: [],
      breed_name: [],
      description: [],
    };
  },
  async mounted() {
    try {
      const response = await getApi.get("/cat-images/");
      this.urls = response.data.urls;
      this.breed_name = response.data.breed_name;
    } catch (error) {
      console.log(error);
    }
  },
  computed: {
  cat_info: function() {
    return this.urls.map((url, index) => {
      return {
        url: url,
        name: this.breed_name[index],
      };
    });
  },
},
};
</script>

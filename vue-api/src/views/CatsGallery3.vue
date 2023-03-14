<template>
  <div>
    <Header/>
    <div class="row">
      <div v-for="(cat, index) in cat_info" :key="index" class="col-md-4">
        <div class="card mb-3">
          <img :src="cat.url" class="card-img-top" alt="Gatito" width="100%">
          <div class="card-body">
            <h5 class="card-title">{{ cat.name }}</h5>
            <p class="card-text">{{ cat.description }}</p>
          </div>
        </div>
      </div>
    </div>
    <PagesFooter/>
  </div>
</template>

<style scoped>

.card {
  margin: 1rem;
  display: flex;
  border-color: #CE7204;
}

.card-img-top{
  height: 300px;
  object-fit: cover;
}



</style>

<script>
import { getApi } from "@/axios-api";
import PagesFooter from "@/components/PagesFooter.vue";
import ScrollToTop from "@/components/ScrollToTop.vue";
import Header from "@/components/Header.vue";

export default {
  components: {
    PagesFooter,
    ScrollToTop,
    Header,
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

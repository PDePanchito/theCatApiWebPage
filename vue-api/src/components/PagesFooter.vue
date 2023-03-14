<template>
<div class="footer">
<nav aria-label="...">
  <ul class="pagination pagination-lg">
    <router-link to="/" id="pagination">
        <li class="page-item" aria-current="page">
        <span class="page-link">1</span>
      </li>
      </router-link>
    <router-link to="/cats/page2" id="pagination">
      <li class="page-item">
        <span class="page-link">2</span>
      </li>
    </router-link>
    <router-link to="/cats/page3" id="pagination">
      <li class="page-item">
        <span class="page-link">3</span>
      </li>
    </router-link>
  </ul>
</nav>
</div>
</template>

<script>
    export default {
        name: "PagesFooter",
    }
</script>

<style scoped>
.footer {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

#pagination {
  color: #d3a31f;
  font-size: 50px;
  text-decoration: none;
  padding: 10px;
}

#pagination:hover {
  color: rgb(245, 236, 220);
}


</style>
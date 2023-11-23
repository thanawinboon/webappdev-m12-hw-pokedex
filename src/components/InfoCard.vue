<script setup>
defineProps({
  pokemon: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <RouterLink :to="{ name: 'pokemon-details', params: { id: pokemon.id } }">
    <div class="info-card">
      <div class="info-card-info">
        <h2>No.{{ pokemon.id }}:</h2>
        <h2>{{ pokemon.name.toUpperCase() }}</h2>
      </div>
      <div class="info-card-img">
        <img :src="pokemon.sprites" :alt="pokemon.name" />
      </div>
    </div>
  </RouterLink>
</template>

<style scoped>
a {
  color: rgb(91, 23, 23);
}
.info-card {
  font-size: 60%;
  padding: 20px;
  width: 250px;
  cursor: pointer;
  border: 1px solid #39495c;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  background-color: rgb(236, 236, 236);
}
.info-card:hover {
  transform: scale(1.05);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2);
}
.info-card-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  text-align: right;
}
.info-card-img img {
  max-width: 90px;
  max-height: 90px;
}
</style>

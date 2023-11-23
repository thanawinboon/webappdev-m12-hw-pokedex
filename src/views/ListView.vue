<script setup>
import { ref, onMounted } from "vue";
import InfoCard from "@/components/InfoCard.vue";

import { db } from "@/firebase/firebase.js";
import { collection, onSnapshot } from "firebase/firestore";

const pokemonList = ref([]);

async function getPokemonListFirebase() {
  onSnapshot(collection(db, "pokemons"), (querySnapshot) => {
    let newPokemonList = [];
    querySnapshot.forEach((doc) => {
      const pokemon = {
        id: doc.id,
        name: doc.data().name,
        name_jp: doc.data().name_jp,
        sprites: doc.data().sprites,
        types: doc.data().types,
        evolves_from: doc.data().evolves_from,
      };
      newPokemonList.push(pokemon);
    });
    pokemonList.value = newPokemonList;
  });
}

onMounted(async () => {
  await getPokemonListFirebase();
});
</script>

<template>
  <div class="background">
    <h1>Pokedex</h1>
    <div class="pokedex-feed">
      <InfoCard v-for="pkm in pokemonList" :key="pkm.id" :pokemon="pkm" />
    </div>
  </div>
</template>

<style scoped>
.background {
  background-color: #ffa1a1;
  padding: 20px;
}
.pokedex-feed {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 15px;
  flex-wrap: wrap;
}
h1 {
  text-align: center;
}
</style>

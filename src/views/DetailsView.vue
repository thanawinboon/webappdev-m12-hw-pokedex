<script setup>
import { ref, onMounted } from "vue";
import { db } from "@/firebase/firebase.js";
import { doc, onSnapshot } from "firebase/firestore";

const currentPokemon = ref(null);
const props = defineProps({
  id: { required: true },
});

async function getPokemonDetailsFirebase(id) {
  onSnapshot(doc(db, "pokemons", id), (result) => {
    const pokemon = {
      id: result.id,
      name: result.data().name,
      name_jp: result.data().name_jp,
      sprites: result.data().sprites,
      types: result.data().types,
      evolves_from: result.data().evolves_from,
    };
    currentPokemon.value = pokemon;
  });
}

onMounted(async () => {
  await getPokemonDetailsFirebase(props.id);
});
</script>

<template>
  <div v-if="currentPokemon">
    <div class="page">
      <div class="pokemon-sprite">
        <img :src="currentPokemon.sprites" :alt="currentPokemon.name" />
      </div>
      <div class="pokemon-info">
        <h3>Pokedex No.{{ currentPokemon.id }}:</h3>
        <h1>
          {{ currentPokemon.name.toUpperCase() }} / {{ currentPokemon.name_jp }}
        </h1>
        <span></span>
        <h3>
          Types: <span v-for="t in currentPokemon.types"> [ {{ t }} ] </span>
        </h3>
        <div class="pokemon-info-evo">
          <h3>Evolution:</h3>
          <span v-if="currentPokemon.evolves_from">
            This Pokemon evolves from {{ currentPokemon.evolves_from.name }}
          </span>
          <span v-else>
            This Pokemon does not have a pre-evolutionary form
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page {
  background-color: #ffa1a1;
  padding: 20px;
}

h1 {
  text-align: center;
}
.pokemon-sprite {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.pokemon-sprite img {
  max-width: 300px;
  max-height: 300px;
  background-color: white;
  border-radius: 20%;
}
.pokemon-info {
  padding: 5px;
  margin: 5px;
  background-color: rgb(236, 236, 236);
  border: 1px solid #39495c;
  display: flex;
  flex-direction: column;
  text-align: center;
  flex-wrap: wrap;
  gap: 0px;
}
.pokemon-info h1 {
  margin: 0px;
}
</style>

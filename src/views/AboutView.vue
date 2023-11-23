<template>
  <div class="about">
    <div class="title">
      <h1>About Pokedex</h1>
    </div>
    <div class="text-wall">
      <p>
        The Pokedex ( illustrated Pokemon encyclopedia ) is an invaluable tool
        to Trainers in the Pokemon world. It gives information about all Pokemon
        in the world that are contained in its database, although it differs in
        how it acquires and presents information over the different media.
        However, they are also only given to a few Trainers at a time, generally
        to the ones that are felt to have exceptional potential and skill.
        Regional Pokedexes give information about Pokemon native to a particular
        region, while the National Pokedex records information about all known
        Pokemon. Professor Laventon is the first known researcher to have
        pioneered the concept of a Pokedex, while the digital version of it is a
        more recent invention created by Professor Oak.
      </p>
      <p>
        Pokedex entries typically describe a Pokemon in only two or three
        sentences. They may give background information on the habitat or
        activities of a Pokemon in the wild or other information on the
        Pokemon's history or anatomy. Pokedex entries also include height,
        weight, cry, footprint (prior to Generation VI), location, other forms,
        and a picture of the Pokemon.
      </p>
    </div>

    <div class="title">
      <h2>About the Student / Assignment</h2>
    </div>
    <div class="text-wall">
      <h3>By: Thanawin Boonpojanasoontorn ( 6280163 )</h3>
      <p>
        Hello, my name is Thanawin Boonpojanasoontorn, a student knowledgable in
        the field of Pokemon. With my personal interest, this assignment can be
        expanded even further with more content and more interesting features if
        given more time.
      </p>
      <p>
        This assignment comes with a python file (located in src/utils) used for
        getting (literally) every information about Pokemon through an API call
        to one of the only few Pokemon API servers out there. Please feel free
        to edit and use it. This assignment could have been even better with the
        direct call to the API server, but due to the assignment's limitation, I
        had to use a python file to get the data instead.
      </p>
    </div>
  </div>
</template>

<style>
@import url("https://fonts.cdnfonts.com/css/sf-pixelate");
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    justify-content: center;
    gap: 10px;
  }

  .title {
    text-align: center;
  }

  p {
    text-align: left;
    margin-bottom: 5px;
  }

  .text-wall {
    font-family: "SF Pixelate", sans-serif;
    font-size: large;
    line-height: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
    width: 70%;
    margin: 0 auto;
    padding: 10px;

    border: 5px solid #39495c;
    background-color: rgb(236, 236, 236);
  }
}
</style>

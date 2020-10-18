<script>
  import Nav from "./Nav.svelte";
  export let segment = "";
</script>

<header>
  <h1> Matheus Avellar </h1>
  <p>
    <i>Sommelier</i> de pizza, programador de inutilidades
  </p>
  <Nav {segment}/>
</header>

<style>
h1 {
  font-size: 5.5rem;
}
p {
  font-size: 1.5rem;
}
@media screen and (max-width: 800px) {
  h1 {
    font-size: 2.75rem;
  }
  p {
    font-size: 1.5rem;
  }
}
</style>
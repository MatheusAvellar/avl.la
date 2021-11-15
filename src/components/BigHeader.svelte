<script>
  import Nav from "./Nav.svelte";
  import Hr from "./Hr.svelte";
  export let segment = "";
</script>

<header>
  <h1> Matheus Avellar </h1>
  <p>
    <i>Connoisseur</i> de pizza, programador de inutilidades
  </p>
  <Nav {segment}/>
  <Hr/>
</header>

<style>
h1 {
  font-size: 3.5rem;
}
p {
  font-size: 1.2rem;
}
@media screen and (max-width: 800px) {
  h1 {
    font-size: 2.5rem;
  }
  p {
    font-size: 1rem;
  }
}
</style>
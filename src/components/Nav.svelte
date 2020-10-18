<script>
  export let segment;
</script>

<nav>
  <ul>
    <li>
    {#if segment}
      <a href=".">home</a>
    {:else}
      <span>home</span>
    {/if}
    </li>
    <li>
    {#if segment != "projetos"}
      <a href="projetos">/projetos</a>
    {:else}
      <span>/projetos</span>
    {/if}
    </li>
    <li>
    {#if segment != "uses"}
      <a href="uses">/uses</a>
    {:else}
      <span>/uses</span>
    {/if}
    </li>
    <li>
    {#if segment != "academic"}
      <a href="academic">/academic</a>
    {:else}
      <span>/academic</span>
    {/if}
    </li>
  </ul>
</nav>

<style>
ul {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}
span {
  color: #444;
}
</style>
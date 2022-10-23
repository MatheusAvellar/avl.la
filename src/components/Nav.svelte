<script>
  export let segment;
</script>

<nav>
  <ul>
    {#if segment}
    <li>
      <a href=".">home</a>
    </li>
    {:else}
    <li class="selected">
      <span>home</span>
    </li>
    {/if}
    {#if segment != "projetos"}
    <li>
      <a href="projetos">/projetos</a>
    </li>
    {:else}
    <li class="selected">
      <span>/projetos</span>
    </li>
    {/if}
    {#if segment != "uses"}
    <li>
      <a href="uses">/uses</a>
    </li>
    {:else}
    <li class="selected">
      <span>/uses</span>
    </li>
    {/if}
    {#if segment != "academic"}
    <li>
      <a href="academic">/academic</a>
    </li>
    {:else}
    <li class="selected">
      <span>/academic</span>
    </li>
    {/if}
  </ul>
</nav>

<style>
nav {
  margin-bottom: 1rem;
}
ul {
  display: flex;
  flex-direction: row;
  align-items: baseline;
  gap: .25rem;
}
ul li {
  position: relative;
}
ul li a[href],
ul li span {
  padding: .25rem .5rem;
  border-radius: 4px;
}
ul li a[href]:hover,
ul li a[href]:active,
ul li a[href]:focus {
  text-decoration: none;
}
ul li:not(.selected):hover a[href] {
  background-color: #f9f9f9;
  background-color: var(--softest-highlight, #f9f9f9);
}
ul li span {
  color: #444;
  color: var(--black, #444);
  background-color: #efefef;
  background-color: var(--soft-highlight, #efefef);
  cursor: default;
}
li.selected::after {
  content: "";
  display: block;
  position: absolute;
  left: 50%;
  width: .75rem;
  height: .2rem;
  margin-top: .125rem;
  border-radius: 1rem;
  transform: translate(-50%);
}
li.selected::after {
  background-color: #0b7dda;
  background-color: var(--accent, #0b7dda);
}
</style>
<script lang="ts">
    import Blurrer from "$lib/Blurrer.svelte";
    import modData from "$lib/mods/data.json";
    
	import { tooltip } from 'svooltip';
	import 'svooltip/styles.css'; // Include default styling
</script>

<h1>Android Compatible Mod List</h1>
<!-- <h3>Find a mod that's not on the list? View details <a on:click={() => window.open("")} href="">here</a>!</h3> -->
<h3>Find a mod that's not on the list? Follow <a href="https://github.com/stardewrocks/android-compatible-mods#readme" target="_blank">this guide</a> to  submit it!</h3>

<table>
    <thead>
        <tr>
            <th>Mod Name</th>
            <th>Status</th>
            <th>Working Version</th>
            <th>Download Link</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        {#each modData as mod}
            <tr>
                <td>{mod.name}</td>
                <td>
                    {#if mod.working == "fully"}
                        <span class="fully">Fully Working</span>
                    {:else if mod.working == "old_version"}
                        <span class="old_version">Old Version Working</span>
                    {:else if mod.working == "not_working"}
                        <span class="not">Not Working</span>
                    {:else if mod.working == "alternate_version"}
                        <span class="alternate">Alternate Version Working</span>
                    {:else}
                        <span class="unknown">Unknown</span>
                    {/if}
                </td>
                <td>{mod.versions.working ? mod.versions.working : "N/A"}</td>
                <td>
                    {#if mod.link.working}
                        <a href={mod.link.working} target="_blank">Download</a>
                    {:else}
                        <span>N/A</span>
                    {/if}
                </td>
                <td
                    use:tooltip={{
                        content: mod.notes ? mod.notes : "None",
                        placement: "top",
                        delay: 0,
                        target: "body",
                    }}
                    on:click={(e) => {
                        //trigger a mouseenter event to show the tooltip
                        const enter = new MouseEvent('mouseenter');
                        enter.initEvent('mouseenter', true, true);
                        e.target?.dispatchEvent(enter);

                        setTimeout(() => {
                            //trigger a mouseleave event to hide the tooltip
                            const leave = new MouseEvent('mouseleave');
                            leave.initEvent('mouseleave', true, true);
                            e.target?.dispatchEvent(leave);
                        }, 2000);
                        
                    }}
                >Press for notes</td>
            </tr>
        {/each}
    </tbody>
</table>


<style lang="scss">
    .fully {
        color: #00ba00;
    }

    .old_version {
        color: #ffba00;
    }
    
    .not {
        color: #ff0000;
    }

    .alternate {
        color: #9bba00;
    }

    table {
        width: 100%;

        &, th, td {
            border: 1px solid #9e5ccd;
            border-collapse: collapse;
        }
    }
    

    
</style>
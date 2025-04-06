<script lang="ts">
import { QueryClient, QueryClientProvider } from "@tanstack/svelte-query";
import { Toaster } from "$lib/components/ui/sonner";
import "../app.css";
let { children } = $props();

const queryClient = new QueryClient();
</script>

<Toaster />

<QueryClientProvider client={queryClient}>
  <main class="flex h-[100dvh] flex-col items-center justify-center">
    {@render children()}
  </main>
</QueryClientProvider>

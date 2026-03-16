import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

const apiTarget = process.env.VITE_API_TARGET ?? "http://localhost:8000";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/book": {
        target: apiTarget,
        changeOrigin: true
      },
      "/status": {
        target: apiTarget,
        changeOrigin: true
      },
      "/author": {
        target: apiTarget,
        changeOrigin: true
      },
      "/genre": {
        target: apiTarget,
        changeOrigin: true
      }
    }
  }
});

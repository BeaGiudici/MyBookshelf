import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/book": {
        target: "http://localhost:8000",
        changeOrigin: true
      },
      "/status": {
        target: "http://localhost:8000",
        changeOrigin: true
      },
      "/author": {
        target: "http://localhost:8000",
        changeOrigin: true
      },
      "/genre": {
        target: "http://localhost:8000",
        changeOrigin: true
      }
    }
  }
});

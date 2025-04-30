/** @type {import('next').NextConfig} */
const nextConfig = {
   output: 'standalone',
  reactStrictMode: true,
  experimental: {
    outputStandalone: true,
  }
};


module.exports = nextConfig;

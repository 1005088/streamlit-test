import '../styles.css';

export const metadata = {
  title: 'Terra Atlas | Earth Terrain',
  description: 'Explore a low-resolution interactive topographic view of Earth.',
};
 
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
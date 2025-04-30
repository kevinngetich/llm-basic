import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import Home from '../src/pages/index'
 
describe('Home', () => {
  it('renders the textarea in page', () => {
    render(<Home />)
 
    const heading = screen.getByRole('textbox', {name: "userQuery"})
 
    expect(heading).toBeInTheDocument()
  })
})
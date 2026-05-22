import { fireEvent, render, screen } from "@testing-library/react";

import Button from "./Button";

describe("Button", () => {
  it("calls onClick handler", () => {
    const onClick = jest.fn();
    render(<Button content="Нажать" onClick={onClick} />);

    fireEvent.click(screen.getByRole("button", { name: "Нажать" }));
    expect(onClick).toHaveBeenCalledTimes(1);
  });
});

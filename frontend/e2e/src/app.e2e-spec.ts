import { browser, by, element } from 'protractor';

describe('Juguetería App E2E Tests', () => {
  beforeEach(() => {
    browser.get('/');
  });

  it('should display welcome message', () => {
    expect(element(by.css('h1')).getText()).toEqual('API de Juguetería funcionando');
  });

  it('should navigate to login page', () => {
    element(by.css('a.login')).click();
    expect(browser.getCurrentUrl()).toContain('/auth/login');
  });

  it('should login with valid credentials', () => {
    element(by.css('a.login')).click();
    element(by.name('correo')).sendKeys('admin@example.com');
    element(by.name('contrasena')).sendKeys('admin123');
    element(by.css('button[type="submit"]')).click();
    expect(element(by.css('h1')).getText()).toEqual('Dashboard');
  });
});
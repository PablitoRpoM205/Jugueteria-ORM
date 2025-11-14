import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, AbstractControl, ValidationErrors } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';

@Component({
    selector: 'app-register',
    templateUrl: './register.component.html',
    styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
    registerForm!: FormGroup;
    isLoading = false;
    errorMessage = '';
    successMessage = '';
    showPassword = false;
    showConfirmPassword = false;

    validationMessages = {
        nombre: '',
        correo: '',
        contrasena: '',
        confirmarContrasena: ''
    };

    constructor(
        private fb: FormBuilder,
        private authService: AuthService,
        private router: Router
    ) { }

    ngOnInit(): void {
        if (this.authService.isAuthenticated()) {
            this.router.navigate(['/dashboard']);
        }

        this.registerForm = this.fb.group({
            nombre: ['', [
                Validators.required,
                Validators.minLength(3),
                this.nombreValidator
            ]],
            correo: ['', [Validators.required, Validators.email]],
            contrasena: ['', [
                Validators.required,
                Validators.minLength(6),
                this.contrasenaValidator
            ]],
            confirmarContrasena: ['', [Validators.required]]
        }, {
            validators: this.passwordMatchValidator
        });

        this.registerForm.valueChanges.subscribe(() => {
            this.updateValidationMessages();
        });
    }

    nombreValidator(control: AbstractControl): ValidationErrors | null {
        if (!control.value) return null;

        const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;

        if (!regex.test(control.value)) {
            return { nombreInvalido: true };
        }

        return null;
    }

    contrasenaValidator(control: AbstractControl): ValidationErrors | null {
        if (!control.value) return null;

        const value = control.value;
        const errors: any = {};

        if (!/[A-Z]/.test(value)) {
            errors.noMayuscula = true;
        }

        if (!/[a-z]/.test(value)) {
            errors.noMinuscula = true;
        }

        if (!/\d/.test(value)) {
            errors.noNumero = true;
        }

        return Object.keys(errors).length > 0 ? errors : null;
    }

    passwordMatchValidator(control: AbstractControl): ValidationErrors | null {
        const password = control.get('contrasena');
        const confirmPassword = control.get('confirmarContrasena');

        if (!password || !confirmPassword) {
            return null;
        }

        return password.value === confirmPassword.value ? null : { passwordMismatch: true };
    }

    updateValidationMessages(): void {
        const nombreControl = this.registerForm.get('nombre');
        const contrasenaControl = this.registerForm.get('contrasena');

        if (nombreControl?.invalid && nombreControl.touched) {
            if (nombreControl.errors?.['required']) {
                this.validationMessages.nombre = 'El nombre es requerido';
            } else if (nombreControl.errors?.['minlength']) {
                this.validationMessages.nombre = 'El nombre debe tener al menos 3 caracteres';
            } else if (nombreControl.errors?.['nombreInvalido']) {
                this.validationMessages.nombre = 'El nombre solo puede contener letras y espacios';
            }
        } else {
            this.validationMessages.nombre = '';
        }

        if (contrasenaControl?.invalid && contrasenaControl.touched) {
            if (contrasenaControl.errors?.['required']) {
                this.validationMessages.contrasena = 'La contraseña es requerida';
            } else if (contrasenaControl.errors?.['minlength']) {
                this.validationMessages.contrasena = 'La contraseña debe tener al menos 8 caracteres';
            } else if (contrasenaControl.errors?.['noMayuscula']) {
                this.validationMessages.contrasena = 'Debe contener al menos una letra mayúscula';
            } else if (contrasenaControl.errors?.['noMinuscula']) {
                this.validationMessages.contrasena = 'Debe contener al menos una letra minúscula';
            } else if (contrasenaControl.errors?.['noNumero']) {
                this.validationMessages.contrasena = 'Debe contener al menos un número';
            }
        } else {
            this.validationMessages.contrasena = '';
        }
    }

    togglePassword(): void {
        this.showPassword = !this.showPassword;
    }

    toggleConfirmPassword(): void {
        this.showConfirmPassword = !this.showConfirmPassword;
    }

    onSubmit(): void {
        if (this.registerForm.invalid) {
            Object.keys(this.registerForm.controls).forEach(key => {
                this.registerForm.get(key)?.markAsTouched();
            });
            this.updateValidationMessages();
            return;
        }

        this.isLoading = true;
        this.errorMessage = '';
        this.successMessage = '';

        const { nombre, correo, contrasena } = this.registerForm.value;

        this.authService.register(nombre, correo, contrasena).subscribe({
            next: (response) => {
                console.log('Registro exitoso:', response);
                this.successMessage = '¡Cuenta creada exitosamente! Redirigiendo al login...';

                setTimeout(() => {
                    this.router.navigate(['/login']);
                }, 2000);
            },
            error: (error) => {
                console.error('Error en registro:', error);

                if (error.error?.detail) {
                    if (typeof error.error.detail === 'string') {
                        this.errorMessage = error.error.detail;
                    } else if (Array.isArray(error.error.detail)) {
                        this.errorMessage = error.error.detail.map((e: any) => e.msg || e).join(', ');
                    }
                } else if (error.status === 400) {
                    this.errorMessage = 'Datos inválidos. Verifica los campos.';
                } else {
                    this.errorMessage = 'Error al crear la cuenta. Intenta de nuevo.';
                }

                this.isLoading = false;
            },
            complete: () => {
                this.isLoading = false;
            }
        });
    }
}
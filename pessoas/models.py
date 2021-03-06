from django.db import models
from unidecode import unidecode

class PessoaManager(models.Manager):
    def filter_by_name(self, entrada):
        termos = [unidecode(t.strip()) for t in entrada.lower().strip().replace('\t', ' ').split(' ') if t]
        if not termos:
            return self.none()
        qs = self.all()
        for termo in termos:
            qs = qs.filter(nome_completo__icontains=termo)
        return qs


# Create your models here.
class Pessoa(models.Model):
    objects = PessoaManager()

    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

    ESTADO_CIVIL = (
        ('1', 'Solteiro'),
        ('2', 'Casado'),
        ('3', 'Separado'),
        ('4', 'Divorciado'),
        ('5', 'Viúvo'),
    )

    ESCOLARIDADE = (
        ('1', 'Ensino Básico'),
        ('2', 'Ensino Fundamental'),
        ('3', 'Ensino Médio'),
        ('4', 'Ensino Técnico'),
        ('5', 'Curso Superior'),
        ('6', 'Especialização'),
        ('7', 'Mestrado'),
        ('8', 'Doutorado'),
    )

    ESTADO = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AM', 'Amanozas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande no Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins'),
    )

    nome = models.CharField(max_length=200, blank=False, default=None)
    sobrenome = models.CharField(max_length=200, blank=False, default=None)
    genero = models.CharField(max_length=1, choices=GENERO, null=True, blank=True, verbose_name='gênero')
    estado = models.CharField(max_length=2, choices=ESTADO, null=True, blank=True)
    escolaridade = models.CharField(max_length=1, choices=ESCOLARIDADE, null=True, blank=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL, null=True, blank=True)

    endereco = models.CharField(max_length=300, blank=True, null=True)
    bairro = models.CharField(max_length=300, blank=True, null=True)
    cidade = models.CharField(max_length=300, blank=True, null=True)
    estado = models.CharField(max_length=2, choices=ESTADO, null=True, blank=True)
    pais = models.CharField(max_length=300, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)

    nome_completo = models.CharField(max_length=200, blank=True, default="")

    def save(self, *args, **kwargs):
        self.nome = ' '.join([x.strip().capitalize() for x in self.nome.replace('\t', ' ').split(' ') if x.strip()])
        self.sobrenome = ' '.join([x.strip().capitalize() for x in self.sobrenome.replace('\t', ' ').split(' ') if x.strip()])
        self.nome_completo = unidecode(" ".join([self.nome, self.sobrenome]).lower())
        return super(Pessoa, self).save(*args, **kwargs)


    def __str__(self):
        return '{0} {1}'.format(self.nome, self.sobrenome)

    @property
    def tratamento(self):
        if self.tratamento_set.filter(ativo=True).exists():
            return self.tratamento_set.filter(ativo=True).order_by('-inicio')[0]